/**
 * Quiz Engine for Digital Textbook
 * Handles both inline quizzes (Učivo pages) and full tests (Testy page)
 */

document.addEventListener('DOMContentLoaded', function() {
  // Initialize inline quizzes on Učivo pages
  initInlineQuizzes();
  
  // Initialize test generator on Testy page
  initTestGenerator();
});

/**
 * Shuffle array using Fisher-Yates algorithm
 */
function shuffleArray(array) {
  const arr = [...array];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

/**
 * Normalize string for comparison (lowercase, trim, remove diacritics)
 */
function normalizeAnswer(str) {
  return str
    .toLowerCase()
    .trim()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '');
}

/**
 * Check if user answer matches any accepted answer
 */
function checkWriteAnswer(userAnswer, acceptedAnswers) {
  const normalizedUser = normalizeAnswer(userAnswer);
  return acceptedAnswers.some(accepted => 
    normalizeAnswer(accepted) === normalizedUser
  );
}

/**
 * Render a single question
 */
function renderQuestion(question, index, namePrefix = 'quiz') {
  const div = document.createElement('div');
  div.className = 'quiz-question';
  div.dataset.id = question.id;
  div.dataset.type = question.type;
  
  // Build image HTML if present
  const imageHtml = question.image 
    ? `<div class="quiz-question-image"><img src="${question.image}" alt="Obrázok k otázke"></div>` 
    : '';
  
  if (question.type === 'single') {
    // Convert 1-based correct index to 0-based for internal use
    const correctIndex = question.correct - 1;
    div.dataset.correct = correctIndex;
    const shuffledOptions = question.options.map((opt, i) => ({ text: opt, originalIndex: i }));
    // Shuffle options
    const shuffled = shuffleArray(shuffledOptions);
    
    div.innerHTML = `
      <p class="quiz-question-text"><strong>${index + 1}.</strong> ${question.question}</p>
      ${imageHtml}
      <div class="quiz-options">
        ${shuffled.map((opt, i) => `
          <label class="quiz-option">
            <input type="radio" name="${namePrefix}-${question.id}" value="${opt.originalIndex}">
            <span>${opt.text}</span>
          </label>
        `).join('')}
      </div>
      <div class="quiz-explanation" hidden>${question.explanation || ''}</div>
    `;
  } else if (question.type === 'write') {
    div.dataset.acceptedAnswers = JSON.stringify(question.accepted_answers);
    div.innerHTML = `
      <p class="quiz-question-text"><strong>${index + 1}.</strong> ${question.question}</p>
      ${imageHtml}
      <div class="quiz-write-input">
        <input type="text" class="quiz-answer-input" placeholder="Napíšte odpoveď...">
      </div>
      <div class="quiz-explanation" hidden>${question.explanation || ''}</div>
    `;
  }
  
  return div;
}

/**
 * Initialize inline quizzes on Učivo pages
 */
function initInlineQuizzes() {
  document.querySelectorAll('.quiz-container').forEach(container => {
    const dataScript = container.querySelector('.quiz-data');
    if (!dataScript) return;
    
    const allQuestions = JSON.parse(dataScript.textContent);
    const count = parseInt(container.dataset.quizCount) || 5;
    
    // Randomly select questions
    const selected = shuffleArray(allQuestions).slice(0, Math.min(count, allQuestions.length));
    
    // Store for checking
    container._questions = selected;
    
    // Render questions
    const questionsDiv = container.querySelector('.quiz-questions');
    selected.forEach((q, i) => {
      try {
        questionsDiv.appendChild(renderQuestion(q, i, 'inline'));
      } catch (e) {
        console.error(`Error rendering question ${q.id}:`, e);
      }
    });
    
    // Track answered questions
    const submitBtn = container.querySelector('.quiz-submit-btn');
    
    container.addEventListener('change', () => {
      updateSubmitButton(container, submitBtn);
    });
    
    container.addEventListener('input', (e) => {
      if (e.target.classList.contains('quiz-answer-input')) {
        updateSubmitButton(container, submitBtn);
      }
    });
    
    submitBtn.addEventListener('click', () => {
      checkQuizAnswers(container);
    });
  });
}

/**
 * Update submit button state based on answered questions
 */
function updateSubmitButton(container, submitBtn) {
  const questions = container._questions;
  let answered = 0;
  
  container.querySelectorAll('.quiz-question').forEach(qDiv => {
    if (qDiv.dataset.type === 'single') {
      if (qDiv.querySelector('input:checked')) answered++;
    } else if (qDiv.dataset.type === 'write') {
      if (qDiv.querySelector('.quiz-answer-input').value.trim()) answered++;
    }
  });
  
  submitBtn.disabled = answered < questions.length;
}

/**
 * Check quiz answers and show results
 */
function checkQuizAnswers(container) {
  let score = 0;
  const questions = container._questions;
  
  container.querySelectorAll('.quiz-question').forEach((qDiv, i) => {
    const question = questions[i];
    let isCorrect = false;
    
    // Disable inputs
    qDiv.querySelectorAll('input').forEach(inp => inp.disabled = true);
    
    if (qDiv.dataset.type === 'single') {
      const selected = qDiv.querySelector('input:checked');
      const correct = parseInt(qDiv.dataset.correct);
      isCorrect = selected && parseInt(selected.value) === correct;
      
      // Highlight correct answer
      qDiv.querySelectorAll('.quiz-option').forEach(opt => {
        const input = opt.querySelector('input');
        if (parseInt(input.value) === correct) {
          opt.classList.add('is-correct');
        }
        if (input.checked && !isCorrect) {
          opt.classList.add('is-incorrect');
        }
      });
    } else if (qDiv.dataset.type === 'write') {
      const userAnswer = qDiv.querySelector('.quiz-answer-input').value;
      const acceptedAnswers = JSON.parse(qDiv.dataset.acceptedAnswers);
      isCorrect = checkWriteAnswer(userAnswer, acceptedAnswers);
      
      const input = qDiv.querySelector('.quiz-answer-input');
      input.classList.add(isCorrect ? 'is-correct' : 'is-incorrect');
      
      // Show accepted answers
      if (!isCorrect) {
        const hint = document.createElement('p');
        hint.className = 'quiz-accepted-answers';
        hint.textContent = `Správne odpovede: ${acceptedAnswers.join(', ')}`;
        qDiv.querySelector('.quiz-write-input').appendChild(hint);
      }
    }
    
    qDiv.classList.add(isCorrect ? 'correct' : 'incorrect');
    
    // Show explanation
    const explanation = qDiv.querySelector('.quiz-explanation');
    if (explanation.textContent) {
      explanation.hidden = false;
    }
    
    if (isCorrect) score++;
  });
  
  // Show results
  const submitBtn = container.querySelector('.quiz-submit-btn');
  submitBtn.hidden = true;
  
  const resultsDiv = container.querySelector('.quiz-results');
  const percentage = Math.round((score / questions.length) * 100);
  resultsDiv.innerHTML = `
    <div class="quiz-score">
      Výsledok: <strong>${score}</strong> z <strong>${questions.length}</strong>
      (${percentage}%)
    </div>
    <button class="quiz-retry-btn" onclick="location.reload()">Skúsiť znova</button>
  `;
}

/**
 * Initialize test generator on Testy page
 */
function initTestGenerator() {
  const configContainer = document.getElementById('test-config');
  const testArea = document.getElementById('test-area');
  const resultsArea = document.getElementById('test-results');
  
  if (!configContainer) return;
  
  const allDataScript = document.getElementById('all-quiz-data');
  if (!allDataScript) return;
  
  const data = JSON.parse(allDataScript.textContent);
  let { questions, topicTree, totalCount } = data;

  // Handle potential double-stringification (fallback)
  if (typeof questions === 'string') {
    try { questions = JSON.parse(questions); } catch (e) {}
  }
  if (typeof topicTree === 'string') {
    try { topicTree = JSON.parse(topicTree); } catch (e) {}
  }
  
  // Store globally for test
  window.allQuestions = questions;
  window.selectedTopics = new Set();
  
  // Build topic tree UI
  buildTopicTree(topicTree);
  
  // Update question count max
  const countInput = document.getElementById('question-count');
  countInput.max = Math.min(100, totalCount);
  
  // Enable start button when topics are selected
  document.getElementById('topic-tree').addEventListener('change', () => {
    updateStartButton();
  });
  
  // Start test button
  document.getElementById('start-test').addEventListener('click', () => {
    startTest();
  });
  
  // Submit test button
  document.getElementById('submit-test').addEventListener('click', () => {
    submitTest();
  });
  
  // Retry button
  document.getElementById('retry-test').addEventListener('click', () => {
    location.reload();
  });
}

/**
 * Build topic selection tree
 */
function buildTopicTree(topicTree) {
  const container = document.getElementById('topic-tree');
  if (!container) return;
  
  container.innerHTML = '';
  
  // Add "Select All" checkbox
  const selectAllDiv = document.createElement('div');
  selectAllDiv.className = 'topic-item topic-select-all';
  selectAllDiv.innerHTML = `
    <label class="topic-checkbox">
      <input type="checkbox" id="select-all-topics">
      <span>Všetko</span>
    </label>
  `;
  container.appendChild(selectAllDiv);
  
  const selectAllCheckbox = selectAllDiv.querySelector('input');
  selectAllCheckbox.addEventListener('change', (e) => {
    container.querySelectorAll('input[type="checkbox"]').forEach(cb => {
      cb.checked = e.target.checked;
      cb.indeterminate = false;
    });
    updateSelectedTopics();
  });
  
  // Build tree for each year
  Object.entries(topicTree).forEach(([yearKey, yearData]) => {
    const yearDiv = document.createElement('div');
    yearDiv.className = 'topic-year';
    
    const yearLabel = yearKey.replace('-rocnik', '. ročník').replace('-', ' ');
    yearDiv.innerHTML = `
      <div class="topic-item topic-year-header">
        <span class="topic-toggle">›</span>
        <label class="topic-checkbox">
          <input type="checkbox" data-year="${yearKey}">
          <span>${yearLabel}</span>
        </label>
      </div>
      <div class="topic-children" style="display: none;"></div>
    `;
    
    const childrenDiv = yearDiv.querySelector('.topic-children');
    const toggle = yearDiv.querySelector('.topic-toggle');
    const yearCheckbox = yearDiv.querySelector(`input[data-year="${yearKey}"]`);
    
    // Toggle expand/collapse
    toggle.addEventListener('click', () => {
      const isExpanded = childrenDiv.style.display !== 'none';
      childrenDiv.style.display = isExpanded ? 'none' : 'block';
      toggle.classList.toggle('expanded', !isExpanded);
    });
    
    // Year checkbox controls all children
    yearCheckbox.addEventListener('change', (e) => {
      childrenDiv.querySelectorAll('input[type="checkbox"]').forEach(cb => {
        cb.checked = e.target.checked;
        cb.indeterminate = false;
      });
      updateSelectedTopics();
      updateParentCheckboxes(container);
    });
    
    // Build parent topics (Brzdy, Pruženie, etc.)
    Object.entries(yearData.parents || {}).forEach(([parentKey, parentData]) => {
      const parentDiv = document.createElement('div');
      parentDiv.className = 'topic-parent';
      
      const parentLabel = parentKey.charAt(0).toUpperCase() + parentKey.slice(1).replace(/-/g, ' ');
      parentDiv.innerHTML = `
        <div class="topic-item topic-parent-header">
          <span class="topic-toggle">›</span>
          <label class="topic-checkbox">
            <input type="checkbox" data-parent="${yearKey}/${parentKey}">
            <span>${parentLabel}</span>
          </label>
        </div>
        <div class="topic-children" style="display: none;"></div>
      `;
      
      const parentChildrenDiv = parentDiv.querySelector('.topic-children');
      const parentToggle = parentDiv.querySelector('.topic-toggle');
      const parentCheckbox = parentDiv.querySelector(`input[data-parent="${yearKey}/${parentKey}"]`);
      
      parentToggle.addEventListener('click', () => {
        const isExpanded = parentChildrenDiv.style.display !== 'none';
        parentChildrenDiv.style.display = isExpanded ? 'none' : 'block';
        parentToggle.classList.toggle('expanded', !isExpanded);
      });
      
      parentCheckbox.addEventListener('change', (e) => {
        parentChildrenDiv.querySelectorAll('input[type="checkbox"]').forEach(cb => {
          cb.checked = e.target.checked;
        });
        updateSelectedTopics();
        updateParentCheckboxes(container);
      });
      
      // Build individual topics
      Object.entries(parentData.topics || {}).forEach(([topicKey, topicData]) => {
        const topicDiv = document.createElement('div');
        topicDiv.className = 'topic-item topic-leaf';
        const topicPath = `${yearKey}/${parentKey}/${topicKey}`;
        topicDiv.innerHTML = `
          <label class="topic-checkbox">
            <input type="checkbox" data-topic="${topicPath}">
            <span>${topicData.name} (${topicData.count})</span>
          </label>
        `;
        
        const topicCheckbox = topicDiv.querySelector('input');
        topicCheckbox.addEventListener('change', () => {
          updateSelectedTopics();
          updateParentCheckboxes(container);
        });
        
        parentChildrenDiv.appendChild(topicDiv);
      });
      
      childrenDiv.appendChild(parentDiv);
    });
    
    container.appendChild(yearDiv);
  });
}

/**
 * Update parent checkboxes based on children state
 */
function updateParentCheckboxes(container) {
  // Update parent checkboxes
  container.querySelectorAll('[data-parent]').forEach(parentCb => {
    const parentPath = parentCb.dataset.parent;
    const children = container.querySelectorAll(`[data-topic^="${parentPath}/"]`);
    const checkedCount = Array.from(children).filter(cb => cb.checked).length;
    
    parentCb.checked = checkedCount === children.length && children.length > 0;
    parentCb.indeterminate = checkedCount > 0 && checkedCount < children.length;
  });
  
  // Update year checkboxes
  container.querySelectorAll('[data-year]').forEach(yearCb => {
    const yearKey = yearCb.dataset.year;
    const children = container.querySelectorAll(`[data-topic^="${yearKey}/"]`);
    const checkedCount = Array.from(children).filter(cb => cb.checked).length;
    
    yearCb.checked = checkedCount === children.length && children.length > 0;
    yearCb.indeterminate = checkedCount > 0 && checkedCount < children.length;
  });
  
  // Update select all checkbox
  const selectAll = container.querySelector('#select-all-topics');
  const allTopics = container.querySelectorAll('[data-topic]');
  const allCheckedCount = Array.from(allTopics).filter(cb => cb.checked).length;
  
  selectAll.checked = allCheckedCount === allTopics.length && allTopics.length > 0;
  selectAll.indeterminate = allCheckedCount > 0 && allCheckedCount < allTopics.length;
}

/**
 * Update selected topics set
 */
function updateSelectedTopics() {
  window.selectedTopics = new Set();
  document.querySelectorAll('[data-topic]:checked').forEach(cb => {
    window.selectedTopics.add(cb.dataset.topic);
  });
  updateStartButton();
}

/**
 * Update start button state
 */
function updateStartButton() {
  const startBtn = document.getElementById('start-test');
  const hasTopics = window.selectedTopics && window.selectedTopics.size > 0;
  startBtn.disabled = !hasTopics;
}

/**
 * Start the test
 */
function startTest() {
  const timeLimit = parseInt(document.getElementById('time-limit').value) || 15;
  const questionCount = parseInt(document.getElementById('question-count').value) || 10;
  
  // Filter questions by selected topics
  const filteredQuestions = window.allQuestions.filter(q => {
    const topicPath = `${q.yearKey}/${q.parentKey}/${q.topicKey}`;
    return window.selectedTopics.has(topicPath);
  });
  
  if (filteredQuestions.length === 0) {
    alert('Žiadne otázky neboli nájdené pre vybrané témy.');
    return;
  }
  
  // Select random questions
  const selected = shuffleArray(filteredQuestions).slice(0, Math.min(questionCount, filteredQuestions.length));
  window.testQuestions = selected;
  
  // Hide config, show test area
  document.getElementById('test-config').style.display = 'none';
  document.getElementById('test-area').style.display = 'block';
  
  // Render questions
  const questionsDiv = document.getElementById('test-questions');
  questionsDiv.innerHTML = '';
  selected.forEach((q, i) => {
    try {
      questionsDiv.appendChild(renderQuestion(q, i, 'test'));
    } catch (e) {
      console.error(`Error rendering question ${q.id}:`, e);
    }
  });
  
  // Update progress
  document.getElementById('test-progress').textContent = `Počet otázok: ${selected.length}`;
  
  // Start timer
  startTimer(timeLimit * 60);
}

/**
 * Start countdown timer
 */
function startTimer(seconds) {
  let remaining = seconds;
  const timerDisplay = document.getElementById('test-timer');
  
  function updateDisplay() {
    const mins = Math.floor(remaining / 60);
    const secs = remaining % 60;
    timerDisplay.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
    
    if (remaining <= 60) {
      timerDisplay.classList.add('timer-warning');
    }
    if (remaining <= 0) {
      timerDisplay.classList.add('timer-expired');
    }
  }
  
  updateDisplay();
  
  window.testTimer = setInterval(() => {
    remaining--;
    updateDisplay();
    
    if (remaining <= 0) {
      clearInterval(window.testTimer);
      submitTest();
    }
  }, 1000);
}

/**
 * Submit test and show results
 */
function submitTest() {
  clearInterval(window.testTimer);
  
  let score = 0;
  const questions = window.testQuestions;
  const details = [];
  
  document.querySelectorAll('#test-questions .quiz-question').forEach((qDiv, i) => {
    const question = questions[i];
    let isCorrect = false;
    let userAnswer = '';
    let correctAnswer = '';
    
    // Disable inputs
    qDiv.querySelectorAll('input').forEach(inp => inp.disabled = true);
    
    if (qDiv.dataset.type === 'single') {
      const selected = qDiv.querySelector('input:checked');
      const correct = parseInt(qDiv.dataset.correct);
      isCorrect = selected && parseInt(selected.value) === correct;
      userAnswer = selected ? question.options[parseInt(selected.value)] : 'Neodpovedané';
      correctAnswer = question.options[correct];
      
      // Highlight correct answer
      qDiv.querySelectorAll('.quiz-option').forEach(opt => {
        const input = opt.querySelector('input');
        if (parseInt(input.value) === correct) {
          opt.classList.add('is-correct');
        }
        if (input.checked && !isCorrect) {
          opt.classList.add('is-incorrect');
        }
      });
    } else if (qDiv.dataset.type === 'write') {
      userAnswer = qDiv.querySelector('.quiz-answer-input').value || 'Neodpovedané';
      const acceptedAnswers = JSON.parse(qDiv.dataset.acceptedAnswers);
      isCorrect = checkWriteAnswer(userAnswer, acceptedAnswers);
      correctAnswer = acceptedAnswers[0];
      
      const input = qDiv.querySelector('.quiz-answer-input');
      input.classList.add(isCorrect ? 'is-correct' : 'is-incorrect');
      
      if (!isCorrect) {
        const hint = document.createElement('p');
        hint.className = 'quiz-accepted-answers';
        hint.textContent = `Správne odpovede: ${acceptedAnswers.join(', ')}`;
        qDiv.querySelector('.quiz-write-input').appendChild(hint);
      }
    }
    
    qDiv.classList.add(isCorrect ? 'correct' : 'incorrect');
    
    // Show explanation
    const explanation = qDiv.querySelector('.quiz-explanation');
    if (explanation && explanation.textContent) {
      explanation.hidden = false;
    }
    
    if (isCorrect) score++;
    
    details.push({
      question: question.question,
      userAnswer,
      correctAnswer,
      isCorrect,
      topic: question.topicName
    });
  });
  
  // Hide submit button
  document.getElementById('submit-test').style.display = 'none';
  
  // Show results summary at top
  const percentage = Math.round((score / questions.length) * 100);
  let gradeClass = 'grade-poor';
  if (percentage >= 90) gradeClass = 'grade-excellent';
  else if (percentage >= 75) gradeClass = 'grade-good';
  else if (percentage >= 50) gradeClass = 'grade-average';
  
  const resultsArea = document.getElementById('test-results');
  resultsArea.style.display = 'block';
  resultsArea.querySelector('#results-score').innerHTML = `
    <div class="score-display ${gradeClass}">
      <span class="score-number">${score}</span>
      <span class="score-separator">/</span>
      <span class="score-total">${questions.length}</span>
      <span class="score-percentage">(${percentage}%)</span>
    </div>
  `;
  
  // Scroll to results
  resultsArea.scrollIntoView({ behavior: 'smooth' });
}

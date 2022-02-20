
function consoleText() {
  var words=['בכל קנייה נתרמים 5 שקלים לאגודה למלחמה בסרטן ', 'אצלנו תמצאו מארזי פרחים שעוד לא ראיתם! ', 'סידורי פרחים שיגרמו לכם להגיד ווואווו '];
  var id='text';
  var visible = true;
  var colorText= '#000';
  var con = document.getElementById('console');
  var letterCount = 1;
  var x = 1;
  var waiting = false;
  var target = document.getElementById(id)
  target.setAttribute('style', 'color:' + colorText)
  window.setInterval(function() {

    if (letterCount === 0 && waiting === false) {
      waiting = true;
      target.innerHTML = words[0].substring(0, letterCount)
      window.setTimeout(function() {
        var usedWord = words.shift();
        words.push(usedWord);
        x = 1;
        target.setAttribute('style', 'color:' + colorText)
        letterCount += x;
        waiting = false;
      }, 1000)
    } else if (letterCount === words[0].length + 1 && waiting === false) {
      waiting = true;
      window.setTimeout(function() {
        x = -1;
        letterCount += x;
        waiting = false;
      }, 1000)
    } else if (waiting === false) {
      target.innerHTML = words[0].substring(0, letterCount)
      letterCount += x;
    }
  }, 120)
  window.setInterval(function() {
    if (visible === true) {
      con.className = 'console-underscore hidden'
      visible = false;
    } else {
      con.className = 'console-underscore'
      visible = true;
    }
  }, 400)
}
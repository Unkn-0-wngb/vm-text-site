(function () {
  var tools = ["KeyI", "KeyJ", "KeyC", "KeyK", "KeyE"];

  function blocked(e) {
    var code = e.code;
    if (code === "F12") return true;
    if ((e.ctrlKey || e.metaKey) && e.shiftKey && tools.indexOf(code) > -1) return true;
    if ((e.ctrlKey || e.metaKey) && !e.shiftKey && !e.altKey && code === "KeyU") return true;
    if (e.metaKey && e.altKey && (code === "KeyI" || code === "KeyJ" || code === "KeyC" || code === "KeyU")) return true;
    return false;
  }

  window.addEventListener(
    "keydown",
    function (e) {
      if (blocked(e)) {
        e.preventDefault();
        e.stopPropagation();
      }
    },
    true
  );

  document.addEventListener("contextmenu", function (e) {
    e.preventDefault();
  });
})();

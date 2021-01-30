/* Toggle function for sidenav */

let navToggled = true;

function toggleNav() {
  if (navToggled) {
    openNav();
    navToggled = false;
  } else {
    closeNav();
    navToggled = true;
  }
  
  function openNav() {
    document.getElementById("sidenav").style.width = "100%";
  }
  
  function closeNav() {
    document.getElementById("sidenav").style.width = "0";
  }
}

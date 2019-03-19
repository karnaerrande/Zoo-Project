alert(3);

window.onscroll = function() {stickyHeader()};

// Get the header
var header = document.getElementById("myHeader");

// Get the offset position of the navbar
// This is the size of the offset when the user is at the very top of the page
var sticky = header.offsetTop;

// Add the sticky class to the header when you reach its scroll position. Remove "sticky" when you leave the scroll position
function stickyHeader() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}

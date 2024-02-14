const redheader = document.getElementById("red_header")
redheader.addEventListener("click", add_class())

function add_class() {
  const header = document.querySelector("header")
  header.classList.add("red")
}

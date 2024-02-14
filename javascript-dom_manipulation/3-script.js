const toggle_header = document.querySelector("#toggle_header")

toggle_header.addEventListener("click", function () {
  const header = document.querySelector("header")
  if (header.classList == "green") {
    header.classList.replace("green", "red")
  }
  else {
    header.classList.replace("red", "green")
  }
})

const header_div = document.querySelector("#red_header")

header_div.addEventListener("click", update_color)

function update_color() {
  const header = document.querySelector("header")
  header.style.color = "#FF0000";
}

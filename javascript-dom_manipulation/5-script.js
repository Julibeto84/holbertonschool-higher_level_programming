const update_header = document.querySelector("#update_header")

update_header.addEventListener("click", function () {
    const header = document.querySelector("header")
    header.replaceWith("New Header!!!")
})

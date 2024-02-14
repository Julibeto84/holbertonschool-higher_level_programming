function text_Content(json) {
    const hello = document.getElementById("hello");
    hello.innerHTML = json.hello;
};
const data = fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
    .then(data => data.json())
    .then(text_Content)

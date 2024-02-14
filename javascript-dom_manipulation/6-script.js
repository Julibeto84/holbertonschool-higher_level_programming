const character = document.getElementById("character");
function text_Content(json) {
    character.textContent = json.name;
}
const data = fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
    .then(data => data.json())
    .then(text_Content)

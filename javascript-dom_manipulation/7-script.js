const list_movies = document.getElementById("list_movies");

function text_Content(json) {
  const results = json.results;
  results.forEach(element => {
    const li_item = document.createElement("li");
    li_item.innerHTML = element.title;
    list_movies.appendChild(li_item);
  });
};
const data = fetch("https://swapi-api.hbtn.io/api/films/?format=json")
  .then(data => data.json())
  .then(text_Content)

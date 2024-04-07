$(function () {
  const iUrl = "https://swapi-api.hbtn.io/api/people/5/?format=json";
  $.get(iUrl, function (data, status) {
    $("DIV#character").text(data.name);
  });
});

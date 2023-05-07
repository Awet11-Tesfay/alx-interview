#!/usr/bin/node

const axios = require('axios');

async function printCharacters(movieId) {
  const filmUrl = `https://swapi.dev/api/films/${movieId}/`;
  const { data } = await axios.get(filmUrl);
  const characters = data.characters;
  for (const character of characters) {
    const { data } = await axios.get(character);
    console.log(data.name);
  }
}

printCharacters(3);

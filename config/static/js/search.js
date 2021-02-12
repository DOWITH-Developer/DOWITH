// challenge List 에 대해서 접근하려면 어떻게 해야될까?

const URL = 'https://gist.githubusercontent.com/Miserlou/c5cd8364bf9b2420bb29/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json';

const challengeList = [];
fetch(URL)
  .then(blob => blob.json())
  .then(data => challengeList.push(...data));

function findMatches(wordToMatch, challengeList) {
  return challengeList.filter(place => {
    const regex = new RegExp(wordToMatch, 'gi');
    return place.city.match(regex) || place.state.match(regex)
  });
}

function displayMatches() {
  const matchArray = findMatches(this.value, challengeList);
  const html = matchArray.map(place => {
    const regex = new RegExp(this.value, 'gi');
    const cityName = place.city.replace(regex, `<span class="hl">${this.value}</span>`);
    const stateName = place.state.replace(regex, `<span class="hl">${this.value}</span>`);
    return `
        <li>
            <span class="name">${cityName}, ${stateName}</span>
        </li>
    `;
  }).join('');
  contentContainer.innerHTML = html;
}

const searchInput = document.querySelector('.searchInput');
const suggestions = document.querySelector('.suggestions');
const contentContainer = document.querySelector('.content');


searchInput.addEventListener('change', displayMatches);
searchInput.addEventListener('keyup', displayMatches);

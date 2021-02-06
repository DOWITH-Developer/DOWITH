// navbar toggle
const navToggle = document.querySelector(".nav-toggle");
const links = document.querySelector(".links");

navToggle.addEventListener("click", function () {
    links.classList.toggle('show-links');
})

// studies items
const studies = [
    {
      id: 1,
      title: "Django",
      category: "breakfast",
      price: 15.99,
      img: "./img/screenshot.png",
      desc: `Lorem ipsum dolor `,
    },
    {
      id: 2,
      title: "JAVA",
      category: "lunch",
      price: 13.99,
      img: "./img/screenshot.png",
      desc: `Lorem ipsum dolor `,
    },
    {
      id: 3,
      title: "Python",
      category: "shakes",
      price: 6.99,
      img: "./img/screenshot.png",
      desc: `Lorem ipsum dolor `,
    },
    {
      id: 4,
      title: "JS",
      category: "breakfast",
      price: 20.99,
      img: "./img/screenshot.png",
      desc: `Lorem ipsum dolor `,
    },
    {
        id: 5,
        title: "Django",
        category: "breakfast",
        price: 15.99,
        img: "./img/screenshot.png",
        desc: `Lorem ipsum dolor `,
      },
      {
        id: 6,
        title: "JAVA",
        category: "lunch",
        price: 13.99,
        img: "./img/screenshot.png",
        desc: `Lorem ipsum dolor `,
      },
      {
        id: 7,
        title: "Python",
        category: "shakes",
        price: 6.99,
        img: "./img/screenshot.png",
        desc: `Lorem ipsum dolor `,
      },
      {
        id: 8,
        title: "JS",
        category: "breakfast",
        price: 20.99,
        img: "./img/screenshot.png",
        desc: `Lorem ipsum dolor `,
      },
  ];


// select items

// get parent element
const sectionCenter = document.querySelector(".section-center");
const btnContainer = document.querySelector(".btn-container");
// display all items when page loads
window.addEventListener("DOMContentLoaded", function () {
    displayItems(studies);
    displayBtns();
});

// 받아와서 내용을 보여준다
function displayItems(studies) {
    let displayStudies = studies.map(function (item) {
        return `<article class="study-item">
            <img src=${item.img} alt=${item.title} class="photo" />
            <div class="item-info">
                <h4>${item.title}</h4>
                <p class="item-text">
                ${item.desc}
                </p>
            </div>
            </article>`;
    });
    displayStudies = displayStudies.join("");
    sectionCenter.innerHTML = displayStudies;
}

function displayBtns() {
    const categories = studies.reduce(
        function (values, item) {
        if (!values.includes(item.category)) {
            values.push(item.category);
        }
        return values;
        },
        ["all"]
    );

    // 이해 
    const categoryBtns = categories
        .map(function (category) {
        return `<button type="button" class="filter-btn" data-id=${category}>
            ${category}
            </button>`;
        })
        .join("");
    btnContainer.innerHTML = categoryBtns;

    displayMatchItems(btnContainer)
    // 함수 분리 가능
}

// 이해 
// 클릭 이벤트에 대해 일치하는 요소에 대해서 반환
function displayMatchItems(btnContainer){
  const filterBtns = btnContainer.querySelectorAll(".filter-btn");
  filterBtns.forEach(function (btn) {
  btn.addEventListener("click", function (e) {
      const category = e.currentTarget.dataset.id;
      const studyCategory = studies.filter(function (studyItem) {
      if (studyItem.category === category) {
          return studyItem;
      }
      });

      if (category === "all") {
          displayItems(studies);
      } else {
          displayItems(studyCategory);
      }
      });
  });
}
const tabs = document.querySelectorAll("[data-tab-target]");
const tabcon = document.querySelectorAll("[data-tab-content]");
const searchList = document.querySelector('.searchList');

tabs.forEach((tab) => {
    tab.addEventListener("click", () => {
        const target = document.querySelector(tab.dataset.tabTarget);
        
        tabcon.forEach((tabc_all) => {
            tabc_all.classList.remove("active");
        });

        tabs.forEach((tabs_all) => {
            tabs_all.classList.remove("active");
        });

        target.classList.add("active");
        tab.classList.add("active");
        searchList.classList.add("search__display__none")
    });
});



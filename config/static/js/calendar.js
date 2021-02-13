let months = ["0월", "1월", "2월", "3월", "4월", "5월", "6월", 
                    "7월", "8월", "9월", "10월", "11월", "12월"];

const calendarTitle = document.querySelector('.calendar_title')
const today = new Date();

//날짜 데이터를 가공하는 함수
function setCalendarData(year, month){        
    let calHtml = "";
    // 이번 달의 첫째 날 객체 반환
    const setDate = new Date(year, month - 1, 1);
    //이번 달의 첫째 날을 구합니다.
    const firstDay = setDate.getDate();
    
    //이번 달의 처음 요일을 구합니다 / (0-6)
    const firstDayName = setDate.getDay();
    
    //이번 달의 마지막 날의 날짜(숫자)를 구합니다.
    const lastDay = new Date(year, month, 0).getDate();
    //지난 달의 마지막 날의 날짜(숫자)를 구합니다.
    const prevLastDay = new Date(year, month-1, 0).getDate();

    let startDayCount = 1;
    let lastDayCount = 1;
    for (let i = 0; i < 6; i++) {
        for (let j = 0; j < 7; j++) {
        if (i == 0 && j < firstDayName) {
            if (j == 0) {
            // 스타일링을 위한 클래스 추가
            calHtml +=
                `<div style='background-color:#FFB3BB;' class='calendar__day horizontalGutter'><span>${(prevLastDay - (firstDayName - 1) + j)}</span><span></span></div>`;
            } else if (j == 6) {
            // 스타일링을 위한 클래스 추가
            calHtml +=
                `<div style='background-color:#FFB3BB;' class='calendar__day'><span>${(prevLastDay - (firstDayName - 1) + j)}</span><span></span></div>`;
            } else {
            // 스타일링을 위한 클래스 추가
            calHtml +=
                `<div style='background-color:#FFB3BB;' class='calendar__day horizontalGutter'><span>${(prevLastDay - (firstDayName - 1) + j)}</span><span></span></div>`;
            }
        }
        else if (i == 0 && j == firstDayName) {
            if (j == 0) {
            // 스타일링을 위한 클래스 추가
            calHtml +=
                `<div style='background-color:#FFE0BB;' class='calendar__day horizontalGutter'><span>${startDayCount}</span><span id='${year}${month}${setFixDayCount(startDayCount++)}'></span></div>`;
            } else if (j == 6) {
            // 스타일링을 위한 클래스 추가
            calHtml +=
                `<div style='background-color:#FFE0BB;' class='calendar__day'><span>${startDayCount}</span><span id='${year}${month}${setFixDayCount(startDayCount++)}'></span></div>`;
            } else {
            // 스타일링을 위한 클래스 추가
            calHtml +=
                `<div style='background-color:#FFE0BB;' class='calendar__day horizontalGutter'><span>${startDayCount}</span><span id='${year}${month}${setFixDayCount(startDayCount++)}'></span></div>`;
            }
        }
        else if (i == 0 && j > firstDayName) {
            if (j == 0) {
            // 스타일링을 위한 클래스 추가
            calHtml +=
                `<div style='background-color:#FFFFBB' class='calendar__day horizontalGutter'><span>${startDayCount}</span><span id='${year}${month}${setFixDayCount(startDayCount++)}'></span></div>`;
            } else if (j == 6) {
            // 스타일링을 위한 클래스 추가
            calHtml +=
                `<div style='background-color:#FFFFBB' class='calendar__day'><span>${startDayCount}</span><span id='${year}${month}${setFixDayCount(startDayCount++)}'></span></div>`;
            } else {
            // 스타일링을 위한 클래스 추가
            calHtml +=
                `<div style='background-color:#FFFFBB' class='calendar__day horizontalGutter'><span>${startDayCount}</span><span id='${year}${month}${setFixDayCount(startDayCount++)}'></span></div>`;
            }
        }
        else if (i > 0 && startDayCount <= lastDay) {
            if (j == 0) {
            // 스타일링을 위한 클래스 추가
            calHtml +=
                `<div style='background-color: var(--sunday);'class='calendar__day horizontalGutter verticalGutter'><span>${startDayCount}</span><span id='${year}${month}${setFixDayCount(startDayCount++)}'></span></div>`;
            } else if (j == 6) {
            // 스타일링을 위한 클래스 추가
            calHtml +=
                `<div style='background-color: var(--saturday);'class='calendar__day verticalGutter'><span>${startDayCount}</span><span id='${year}${month}${setFixDayCount(startDayCount++)}'></span></div>`;
            } else {
            // 스타일링을 위한 클래스 추가
            calHtml +=
                `<div style='background-color: var(--base);'class='calendar__day horizontalGutter verticalGutter'><span>${startDayCount}</span><span id='${year}${month}${setFixDayCount(startDayCount++)}'></span></div>`;
            }
        }
        // 이번 달 이후의 달 표시
        // else if (startDayCount > lastDay) {
        //     if (j == 0) {
        //     // 스타일링을 위한 클래스 추가
        //     calHtml +=
        //         `<div style='background-color:#BBFFC9;' class='calendar__day horizontalGutter verticalGutter'><span>${lastDayCount++}</span><span></span></div>`;
        //     } else if (j == 6) {
        //     // 스타일링을 위한 클래스 추가
        //     calHtml +=
        //         `<div style='background-color:#BBFFC9;' class='calendar__day verticalGutter'><span>${lastDayCount++}</span><span></span></div>`;
        //     } else {
        //     // 스타일링을 위한 클래스 추가
        //     calHtml +=
        //         `<div style='background-color:#B9E1FF;' class='calendar__day horizontalGutter verticalGutter'><span>${lastDayCount++}</span><span></span></div>`;
        //     }
        // }
        }
    }
    console.log(`변수로 넘어오는 달 : ${month}`)
    calendarTitle.innerHTML = months[(+month)%13];
    console.log(`제목 : ${months[(+month)%13]}`)
    document
        .querySelector(".calendar")
        .insertAdjacentHTML("beforeend", calHtml);
};


const setFixDayCount = number => {
    let fixNum = "";
    if (number < 10) {
        fixNum = "0" + number;
    } else {
        fixNum = number;
    }
    return fixNum;
};



// TODO 
// 1. 다음 달 표시
//  - after 버튼을 클릭하면 다음 달 (년도를 신경쓰지 말고 구해보자)
//  - 저번 달 보여주는 걸 지우는 함수
// 2. 지난 달 표시 
// 3. 년도가 바뀔 때 연도를 바꿔주는 함수 + 년도가 바뀔 때 함수 위에 이름도 
// 4. 날짜 선택자로 선택 (완료)
// 5. 오늘 날짜 표시
// 6. 리펙토링 범수쓰 함수 구성 참고 
// 7. 일주일 단위 보여주기
let thisMonth = today.getMonth()+1;
let thisYear = today.getFullYear();
let plus = 1;
let minus = 1;

function selectMonth(thisMonth, thisYear){
    if (thisMonth < 10) {
        setCalendarData(thisYear, "0" + thisMonth);
    } else {
        setCalendarData(thisYear, "" + thisMonth);
    }
    console.log(`${thisMonth}+${thisYear}`)
}



let afterMonth = document.querySelector('.after');
afterMonth.addEventListener('click', () => {
    thisMonth += plus;
    document.querySelector(".calendar").innerHTML = ""
    thisYear = (thisMonth === 13) ? thisYear + 1 : thisYear;
    thisMonth = (thisMonth === 13) ? 1 : thisMonth;
    console.log(`이번 달 : ${thisMonth}`);
    console.log(`이번 년 : ${thisYear}`);
    selectMonth(thisMonth, thisYear);
})

let previousMonth = document.querySelector('.previous');
previousMonth.addEventListener('click', () => {
    thisMonth -= minus;
    document.querySelector(".calendar").innerHTML = ""
    thisYear = (thisMonth === 0) ? thisYear - 1 : thisYear;
    thisMonth = (thisMonth === 0) ? 12 : thisMonth;
    console.log(`이번 달 : ${thisMonth}`);
    console.log(`이번 년 : ${thisYear}`);
    selectMonth(thisMonth, thisYear);
})

   // 20210222
    // 년 월 일 
// console.log(today.getDate());
// console.log(thisMonth, thisYear)
// const thisDay = document.querySelector(``)
window.addEventListener('DOMContentLoaded', selectMonth(thisMonth, thisYear))

const todayId = (thisMonth < 10) ? `${thisYear}${'0' + thisMonth}${today.getDate()}`: `${thisYear}${thisMonth}${today.getDate()}`;
const todaySelector = document.getElementById(`${todayId}`);
const todayContainer = todaySelector.parentNode;
// style 에서 outline 을 추가만 할꺼야
todayContainer.style.borderColor = "red";
// todayContainer.setAttribute("style", "background-color: var(--base);");
// 이번 달 모든 span 을 가져온다
// 그 중 id 가 오늘 날짜


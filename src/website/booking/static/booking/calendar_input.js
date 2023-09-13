let currently_selected_date = null;


function make_data_list(data) {

}

const BasicCalendarButtonClass = "unselected-button font-normal hover:font-bold disabled:hover:bg-transparent hover:bg-sky-800 hover:opacity-50 hover:text-white h-8 w-full grid place-content-center";
const StartCalendarButtonClass = "focus:bg-sky-700 selected-button font-normal hover:font-bold rounded-l-lg bg-sky-800 text-white h-8 w-full disabled:opacity-75 grid place-content-center";
const EndCalendarButtonClass = "focus:bg-sky-700 selected-button font-normal hover:font-bold rounded-r-lg bg-sky-800 text-white h-8 w-full disabled:opacity-75 grid place-content-center";
const SelectedCalendarButtonClass = "focus:bg-blue-200 selected-button font-normal hover:font-bold bg-blue-100 text-sky-800 h-8 w-full disabled:opacity-75 grid place-content-center";
const StartEndCalendarButtonClass = "selected-button font-normal hover:font-bold rounded-lg bg-sky-800 text-white h-8 w-full disabled:opacity-75 grid place-content-center";

function calendar_button(x, y, text) {
    return `<button id="cal-btn-${x}-${y}"class="${BasicCalendarButtonClass}" onClick="calendar_button_clicked(this)">${text}</button>`;
}

function make_empty_calendar() {

    let days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'];
    let calendar = "";
    for (let x = 0; x < 7; x++) {
        let new_col = `<div class="w-1/7">\n<div class="text-silver">${days[x]}</div>\n`;
        for (let y = 0; y < 6; y++) {
            new_col += calendar_button(x, y, '');
            new_col += '\n';
        }
        new_col += '</div>';
        calendar += new_col;
    }

    return '<div class="grid grid-cols-7 md:w-2/3">\n' + calendar + '\n</div>';
}


function days_in_month(month, year) {
  return new Date(parseInt(year), parseInt(month), 0).getDate();
}

function first_day_in_month(month, year) {
    return new Date(parseInt(year), parseInt(month) - 1, 1).getUTCDay();
}

const calendar = make_empty_calendar();
const calendar_body = document.getElementById('calendar-body');
calendar_body.innerHTML = calendar;

const CalendarData = new Set();

const byId = (id) => document.getElementById(id);
const byCoords = (x, y) => document.querySelector(`#cal-btn-${x}-${y}`);
const monthSelect = byId("month-select");
const yearSelect = byId("year-select");

const populate_calendar = () => { 
    const month_length = days_in_month(monthSelect.value, yearSelect.value);
    const offset = first_day_in_month(monthSelect.value, yearSelect.value) - 1;

    let day_in_month = 0;

    for (let y = 0; y < 6; y++) {
        for (let x = 0; x < 7; x++) {
            byCoords(x, y).className = BasicCalendarButtonClass;
            if ((y != 0 || x > offset) && day_in_month++ < month_length) {
                byCoords(x, y).innerHTML = day_in_month;
                byCoords(x, y).disabled = false;

                let text_date = `${yearSelect.value}-${monthSelect.value}-${day_in_month}`
                let current_date = new Date(text_date);
                byCoords(x, y).dataset.date = text_date;

                if (text_date === currently_selected_date) {
                    byCoords(x, y).className = StartEndCalendarButtonClass;
                }

                const key = `${yearSelect.value}-${monthSelect.value}`;
                CalendarData.forEach((range) => {
                    let start = new Date(range["start"]);;
                    let end = new Date(range["end"]);
                    if (start < current_date && current_date < end) {
                        byCoords(x, y).className = SelectedCalendarButtonClass;
                    } else if (start.getTime() === current_date.getTime()) {
                        byCoords(x, y).className = StartCalendarButtonClass;
                    } else if (end.getTime() === current_date.getTime()) {
                        byCoords(x, y).className = EndCalendarButtonClass;
                    }

                });
            } else {
                byCoords(x, y).innerHTML = "";
                byCoords(x, y).disabled = true;
            }
        }

    }
}

const calendar_left = () => {
    if (monthSelect.value > 1) {
        monthSelect.value--;
    } else {
        yearSelect.value--;
        monthSelect.value = 12;
    }
    populate_calendar();
}

const calendar_right = () => {
    if (monthSelect.value < 12) {
        monthSelect.value++;
    } else {
        yearSelect.value++;
        monthSelect.value = 1;
    }
    populate_calendar();
}

populate_calendar();

[monthSelect, yearSelect].forEach((domNode) => { 
  domNode.addEventListener("change", populate_calendar);
})

document.addEventListener("keydown", (event) => {
    const btn = document.activeElement;
    if (event.key === "Backspace" && btn.classList.contains("selected-button")) {
        let selected_range;
        const selected_date = new Date(btn.dataset.date)
        CalendarData.forEach((range) => {
            let start = new Date(range["start"]);
            let end = new Date(range["end"]);

            if (start <= selected_date && selected_date <= end) {
                selected_range = range;
            }
            
        });

        CalendarData.delete(selected_range);
        populate_calendar();
    }
});

function calendar_button_clicked(btn) {
    if (btn.classList.contains("unselected-button")) {
        if (currently_selected_date === null) {
            btn.className = StartEndCalendarButtonClass;
            currently_selected_date = btn.dataset.date;
        } else {
            let temp1 = new Date(currently_selected_date);
            let temp2 = new Date(btn.dataset.date);
            let date1, date2;

            currently_selected_date = null;
            if (temp1 < temp2) {
                date1 = temp1;
                date2 = temp2;
            } else if (temp2 < temp1) {
                date1 = temp2;
                date2 = temp1;
            } else {
                populate_calendar();
                return;
            }

            for (const range of CalendarData) {
                start = new Date(range["start"]);
                end = new Date(range["end"]);

                if ((date1 <= start && start <= date2) || (date1 <= end && end <= date2)) {
                    populate_calendar();
                    return;
                } 
            };

            CalendarData.add({"start": date1.toISOString().split('T')[0], "end": date2.toISOString().split('T')[0]});
            populate_calendar();
        }
    } else {
        currently_selected_date = null;
        populate_calendar();
    }
}

async function send_calendar_data() {
    const url = "flightsapi/";
    const response = await fetch(url, {
        method: "POST", // *GET, POST, PUT, DELETE, etc.
        mode: "cors", // no-cors, *cors, same-origin
        cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
        credentials: "same-origin", // include, *same-origin, omit
        headers: {
          "Content-Type": "application/json",
          // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        redirect: "follow", // manual, *follow, error
        referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
        body: JSON.stringify(Array.from(CalendarData)), // body data type must match "Content-Type" header
    });

    const json_response = await response.json();
    console.log(json_response);
}

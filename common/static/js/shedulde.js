function daysInMounth(date) {
    let days_count = new Date(date.getFullYear(), date.getMonth(), 0).getDate()
    console.log('Days in month', days_count)
    return days_count
}

function getNameOfDay(date) {

    let day_index = date.getDay()

    let days = {
        0: 'Вс',
        1: 'Пн',
        2: 'Вт',
        3: 'Ср',
        4: 'Чт',
        5: 'Пт',
        6: 'Сб',
    }

    return days[day_index]
}

function create_cell(data) {
    let cell = document.createElement('td');

    cell.innerText = data

    return cell
}

function create_row(cells = []) {
    let row = document.createElement('tr');

    for (let cell of cells) {
        row.append(cell)
    }

    return row
}


export default {
    init: () => {
        let now_date = new Date(Date.now());

        for (let sh_el of document.getElementsByClassName('shedulde')) {
            let table = document.createElement('table');
            let body = document.createElement('tbody');

            let days_row = create_row();
            let name_of_day = create_row();

            for (let a = 1; a <= daysInMounth(now_date); a++) {
                name_of_day.append(create_cell(getNameOfDay(new Date(now_date.getFullYear(), now_date.getMonth(), a))));
                days_row.append(create_cell(a));
            }

            body.append(name_of_day);
            body.append(days_row);

            table.append(body);
            sh_el.append(table);
        }
    }
}
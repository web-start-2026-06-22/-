window.addEventListener('load', bind)

function bind() {

    const btn1 = document.querySelector('#btn1');
    btn1.addEventListener('click', function () {

        // 1. ajax 객체 생성
        const xhr = new XMLHttpRequest();

        // 2. 보낼 준비
        // 방식method, 주소
        xhr.open('GET', 'https://jsonplaceholder.typicode.com/users');

        // 3. 보내기
        xhr.send()

        // 4. 결과 활용
        xhr.onload = function () {
            console.log('다녀왔어');
            console.log(xhr.responseText);

            // 깜짝 퀴즈
            // 두 번째 사람의 이름을 출력.
            // 세 번째 사람의 lat를 출력.

            const xhrText = JSON.parse(xhr.responseText);
            console.log(xhrText[1].name);
            console.log(xhrText[2]['address']['geo'].lat);

        }

    })

    const btn2 = document.querySelector('#btn2');
    btn2.addEventListener('click', function () {

        // 1. ajax 객체 생성
        const xhr = new XMLHttpRequest();

        // 2. 보낼 준비
        // 방식method, 주소
        xhr.open('GET', '19_json.html');

        // 3. 보내기
        xhr.send()

        console.log('[' + xhr.responseText + ']');

        // 4. 결과 활용
        xhr.onload = function () {
            console.log('다녀왔어');
            console.log(xhr.responseText);
        }

    })

    const btn3 = document.querySelector('#btn3');
    btn3.addEventListener('click', function () {

        const key = '44803eb181a2488a11cc733e9590d4c4a279dc6df4aa326dca234e6fd8fe4a6f';

        let url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst'
        url += '?'
        url += 'serviceKey=' + key
        url += '&numOfRows=1000'
        url += '&pageNo=1'
        url += '&dataType=JSON'
        url += '&base_date=20260722'
        url += '&base_time=1500'
        url += '&nx=63'
        url += '&ny=110'

        // 1. ajax 객체 생성
        const xhr = new XMLHttpRequest();

        // 2. 보낼 준비
        // 방식method, 주소
        xhr.open('GET', url);

        // 3. 보내기
        xhr.send()

        // 4. 결과 활용
        xhr.onload = function () {
            // console.log(xhr.responseText);
            const data = JSON.parse(xhr.responseText);
            console.log(data);

            console.log(data.response.body.items.item[0].category);
            console.log(data.response.body.items.item[0].fcstValue);
            console.log(data.response.body.items.item[0].fcstTime);

            // category가 T1H(기온), RN1(강수량), REH(습도)

            let item = data.response.body.items.item
            // for (let i = 0; i < item.length; i++) {
            //     if (item[i].category == 'T1H') {
            //         console.log(item[i]);
            //     } else if (item[i].category == 'RN1') {
            //         console.log(item[i]);
            //     } else if (item[i].category == 'REH') {
            //         console.log(item[i]);
            //     }

            // }

            let filtered = item.filter(function (data) {
                if (data.category == 'T1H'
                    || data.category == 'RN1'
                    || data.category == 'REH')
                    return true;
            })
            // console.log(filtered);

            // 문제1 :
            // 예측카테고리 | 예측시간 | 값


            // 배열에 담고, join('|'), innerText하려 했는데 필요없을 듯.
            let q1_arr = [];
            let q1_list = [];
            // let q1_str = ''; 필요없어져서 주석처리.
            // join으로 문자열로 만들고 한 줄 한 줄 넣어주려 했는데 테이블이 적합.
            for (let i = 0; i < item.length; i++) {
                q1_arr.push(item[i].category);
                q1_arr.push(item[i].fcstTime);
                q1_arr.push(item[i].fcstValue);
                // 3개씩 자르기                 
                if (i % 3 == 0) {
                    q1_list.push(q1_arr.slice(i, i + 3));
                }
            }
            // console.log(q1_arr); // 전체 리스트
            console.log(q1_list); // 배열을 3개 단위로 나눈 것.

            // 테이블 형태로 담아주고 웹에 뿌리기.
            let q1_table = document.querySelector('.q1');
            for (let i = 0; i < q1_list.length; i++) {
                let tr = document.createElement('tr');
                // console.log(tr);
                for (let j = 0; j < q1_list[i].length; j++) {
                    let td = document.createElement('td');
                    tr.append(td);
                    td.textContent = q1_list[i][j];
                    // console.log(td);
                }
                q1_table.append(tr);
            }
            // 문제2
            // 시간 | 온도 | 습도 | 강수량 (시간에 맞게)
            // 예측시각에 맞게니까 예측시간을 키값으로 주고
            // 해당하는 시각의 데이터들을 json이든 배열으로든 구성해서
            // 1번처럼 넣어주기. 형태는 문제에 맞게 가공해서.

            // let q2_arr = [];
            // let q2_list = [];

            j = {};

            // 그럼 filtered 위에서 썼던 거 재활용하면 되겠구나.
            for (let i = 0; i < filtered.length; i++) {
                if (j[filtered[i].fcstTime] == undefined) { // 없으면
                    j[filtered[i].fcstTime] = {} // 초기화. 생성.
                }
                j[filtered[i].fcstTime][filtered[i].category] = filtered[i].fcstValue;
                // q2_arr.push(item[i].fcstTime);
                // category였네 아래 저 세가지가
                // q2_arr.push(item[i].T1H);
                // q2_arr.push(item[i].REH);
                // q2_arr.push(item[i].RN1);
                // if (q2_arr.indexOf(item[i].fcstTime) != -1) {
                //     if (item[i].category == 'T1H') {
                //         q2_arr.push(item[i].fcstValue);
                //     }

                //     else if (item[i].category == 'RN1') {
                //         q2_arr.push(item[i].fcstValue);
                //     }

                //     else if (item[i].category == 'REH') {
                //         q2_arr.push(item[i].fcstValue);
                //     }
                // } else {
                //     q2_arr.push(item[i].fcstTime);
                // }

            }
            console.log(j); // 전체 값 잘 가져와지는지 체크.

            let keys = Object.keys(j);
            // let values = Object.values(j);

            let q2_table = document.querySelector('.q2');

            for (let i = 0; i < keys.length; i++) {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                <td>${keys[i]}</td>
                <td>${j[keys[i]]['T1H']}</td>
                <td>${j[keys[i]]['REH']}</td>
                <td>${j[keys[i]]['RN1']}</td>
                `
                q2_table.append(tr);
            }
            // q2_table.innerHTML = '';
            // for (let i = 0; i < q2_list.length; i++) {
            //     let tr = document.createElement('tr');
            //     // console.log(tr);
            //     for (let j = 0; j < q2_list[i].length; j++) {
            //         let td = document.createElement('td');
            //         tr.append(td);
            //         td.textContent = q2_list[i][j];
            //         // console.log(td);
            //     }
            //     q2_table.append(tr);
            // }
        }

    })

    // bt4를 클릭하면
    // https://jsonplaceholder.typicode.com/users
    // 10명의 정보 중 id, name, zipcode, 회사이름을 html로 표시



    const btn4 = document.querySelector('#btn4');
    btn4.addEventListener('click', function () {

        const xhr = new XMLHttpRequest();

        xhr.open('GET', 'https://jsonplaceholder.typicode.com/users');

        xhr.send()

        xhr.onload = function () {
            const xhrText = JSON.parse(xhr.responseText);
            console.log(xhrText);

            let q3 = document.querySelector('.q3');
            let q3_arr = [];
            let q3_json = {};
            let q3_list = [];

            for (let i = 0; i < xhrText.length; i++) {
                q3_arr.push(xhrText[i]['id']);
                q3_arr.push(xhrText[i]['name']);
                q3_arr.push(xhrText[i]['address']['zipcode']);
                q3_arr.push(xhrText[i]['company']['name']);
            }
            console.log(q3_arr); // 전체값 체크

            for (let i = 0; i < q3_arr.length; i++) {
                if (i % 4 == 0) {
                    q3_list.push(q3_arr.slice(i, i + 4));
                }
            }
            console.log(q3_list);
            // json이 나을 것 같은데

            // let q3_keys = Object.keys(xhrText);
            // for(let i = 0; i < xhrText.length; i++){
            //     if(q3_json[key[i]] == undefined){
            //         q3_json[key[i]] = {}
            //     }

            // }

            for (let i = 0; i < q3_list.length; i++) {
                const tr = document.createElement('tr');


                // console.log(`리스트의 ${i}번째 줄 ${j}번째 칸 : ${q3_list[i][j]}`);
                tr.innerHTML = `
                    <td>${q3_list[i][0]}</td>
                    <td>${q3_list[i][1]}</td>
                    <td>${q3_list[i][2]}</td>
                    <td>${q3_list[i][3]}</td>
                    `
                q3.append(tr);

            }

        }
    })
    const btn5 = document.querySelector('#btn5');
    btn5.addEventListener('click', function () {

        let a = undefined;
        try {
            a.push(1)
        } catch (e) {
            console.log(e);
        }

        const url = 'https://jsonplaceholder.typicode.com/users';

        // fetch(주소, 옵션json)
        fetch(url, {
            method: 'GET'
        }).then(function (response) {
            return response.json();
        }).then(function (data) {
            console.log(data)
        }).catch(function (error) {
            console.error(error);
        })

    })

    const btn6 = document.querySelector('#btn6');
    btn6.addEventListener('click', function () {

        debugger;

        console.log('btn6 클릭');
        debug();
        console.log('끝');

    })
}

function debug() {

    let a = 1;

    console.log(a);
}

let a = {
    a: 1,
    b: 2,
    a: 3
}
console.log(a);

// key가 없으면 만들고
// key가 있으면 그 값에 + 1을 한다.
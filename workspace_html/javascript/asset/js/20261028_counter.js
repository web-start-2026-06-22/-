window.onload = () => {
    let a = [1, 5, 3, 4, 78, 5, 5, 1];
    let j = {};
    for (let i = 0; i < a.length; i++) {

        // console.log(a[i]);
        if (j[a[i]] == undefined) {
            j[a[i]] = 1;
        } else
            j[a[i]] += 1;
        // j[`${a[i]}`] 
    }
    console.log('j:', j);

    const names = ['규혁', '근욱', '영욱', '상우', '용준', '도영', '재성', '준석'];

    let name_len = names.length;

    // console.log(name_len);

    // console.log(names.length); // 8
    // 문제1. 랜덤으로 1명을 고른다.
    // 문제2. 1.의 행동을 100번 반복한다.
    // 문제3. 누가 몇 표가 나왔는지 출력한다.
    // 문제4. 가장 많은 득표 수는 누구, 몇 표만 출력한다.

    // 문제1. 랜덤으로 1명을 고른다.
    console.log(names[parseInt(Math.random() * name_len)]);
    j = {};
    // 문제2. 1.의 행동을 100번 반복한다.
    for (let i = 0; i < 100; i++) {
        let randName = names[parseInt(Math.random() * name_len)];
        // console.log('랜덤 이름:', randName);

        // if (j[randName] == undefined)
        if (!j[randName])
            j[randName] = 1;
        // console.log(i, randName);
        j[randName] += 1; // 여기 구문까지 해서 이미 데이터는 다 들어감.

    }
    // 문제3. 누가 몇 표가 나왔는지 출력한다.
    console.log(j);

    // 문제4. 가장 많은 득표 수는 누구, 몇 표만 출력한다.

    // Object.keys, Object.values = 19_json 참고.
    let keys = Object.keys(j);
    let values = Object.values(j);
    j = {};
    // 선언해놓고 안 씀
    // let max_people = '';
    let max_vote = values[0];

    // index 저장용 변수.
    let index_store = 0;
    // console.log(keys);
    // console.log(values);

    for (let i = 0; i < values.length; i++) {
        if (max_vote < values[i]) {
            max_vote = values[i];
            // 해당 인덱스를 담아준다.
            index_store = i;
        }
    }
    // console.log(max_vote);
    // console.log(keys[index_store]);
    console.log('가장 많은 득표를 받은 사람:', keys[index_store]);
    console.log('가장 많은 득표 수:', max_vote);
}
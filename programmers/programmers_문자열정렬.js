function solution(my_string) {
    var answer = new Array();
    let cur_char, tmp;

    for( let i=0; i<my_string.length ; i++){
        cur_char = my_string[i].toLowerCase();

        answer[i] = cur_char;

        for ( let j=i-1; j >-1; j--){
            if( answer[j] > answer[j+1]) {
                tmp = answer[j];
                answer[j] = answer[j+1];
                answer[j+1] = tmp;
            }
        }   
        // console.log(answer);
    };
    answer = answer.join("");
    return answer;
}

const result = solution('heLLo');
console.log(result);
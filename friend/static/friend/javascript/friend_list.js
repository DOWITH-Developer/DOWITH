const giveMotivation = async (id) => {
    const url = "/friend/motivate/";
    //이미 challengeUrl이 존재한다면 axios 실행을 안해도 됨. 그 조건을 따지기 위한 코드
    
    let message = confirm("콕 찌르시겠습니까?")

    if (message) {
        const {data} = await axios.post(url, {
            id
        })

        alert(data.user + '님을 콕 찌르셨습니다.')
    }
}


//콕 찌르기의 위치가 정해지면 수정해야 함
const removeMotivation = async (id=null) => {
    const url = "/friend/motivate/remove/";

    if (id === null) {

        let = message = confirm('모든 콕 찌르기를 지우시겠습니까?')

        if (message) {
            const {data} = await axios.post(url, {
                id
            })

            if (data.status == true) {
                const allMotivations = document.querySelectorAll('.friend__motivation__from__friend')

                allMotivations.forEach(motivation => motivation.remove())

                alert('모든 콕 찌르기를 지우셨습니다.')
            } else {
                alert('다시 실행해 주세요.')
            }
        }

    } else {

        let = message = confirm('해당 콕 찌르기를 지우시겠습니까?')

        if (message) {
            
            const motivationTarget = document.querySelector(`.motivation-${id}`)
            motivationTarget.remove()

            const {data} = await axios.post(url, {
                id
            })

            alert('지웠습니다.')
        }

    }


}
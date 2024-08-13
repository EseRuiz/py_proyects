const {createApp, ref} = Vue;

const app = createApp({
    // template:`
    //     <h1>{{message}}</h1>
    //     <p> {{author}} </p>    
    // `,
    setup(){
        const message = ref('soy Batman');
        const author = ref('Bruce wayne')

        const changeNAme = () => {
            message.value = 'Hola, soy Goku';
            author.value = 'goku'
        }
        // setTimeout(() => {
        //     message.value = 'Hola, soy Goku';
        //     author.value = 'goku'
        // }, 1000)
        return {
            message,
            author,
            changeNAme,
        }
    }
});


app.mount('#myApp')
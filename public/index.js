const API_URL = "http://127.0.0.1:8000/animals/"

async function loadAnimals() {
    const response = await axios.get(API_URL)
    const animals = response.data

    const listAnimals = document.getElementById("list-aniamls")

    listAnimals.innerHTML = ''

    animals.forEach(animal => {
        const item = document.createElement("li")
        item.innerHTML = animal.name
        listAnimals.appendChild(item)
    });
}

function handleForm() {
    const formAnimal = document.getElementById("formAnimals")
    const inputAnimalName = document.getElementById("name")

    formAnimal.onsubmit = async (event) => {
        event.preventDefault();
        const animalName = inputAnimalName.value
        
        await axios.post(API_URL, {
            name: animalName,
            age: 7,
            sex: "f",
            color: "white"
        })

        inputAnimalName.value = ""
        loadAnimals()
    }
}

function app() {
    console.log("application initiallized");
    loadAnimals();
    handleForm();
}

app()
const fs = require('fs/promises')
const prompt = require('prompt-sync')()

// This function will display all of the courses currently in the system.
// The output will be:
// CODE, Name, Capacity
// INFS3201, Web Tech II, 34
// INFS1201, Programming, 120
//
// If there are no courses then you should see the message "No courses".
async function listAllCourses() {
    let raw = await fs.readFile('courses.json', 'utf8')
    let data = await JSON.parse(raw)
    if (data.length === 0) {
        console.log('No courses found')
    }
    else {
        console.log('code, name, capacity')
        for (c of data) {
            console.log(`${c.code}, ${c.name}, ${c.capacity}`)
        }
    }
}

// This function will display a single course given the code (i.e. INFS3201).  The format of the output
// must be:
//    Code: INFS3201
//    Name: Web Technologies II
//    Capacity: 24
// If there is no course with the given code then print the message "Course not found"
async function findCourseByCode(code) {
    let raw = await fs.readFile('courses.json', 'utf8')
    let data = await JSON.parse(raw)
    for (c of data) {
        if (c.code === code) {
            console.log(`Code: ${c.code}`)
            console.log(`Name: ${c.name}`)
            console.log(`Capacity: ${c.capacity}`)
            console.log("")
            return
        }
    }
    console.log('No course found')
}

// This function will display all courses with a minimum of "cap" capacity.  For example if you put
// the parameter cap at 30, we would see courses with a capacity 30 or larger.  The output should be
// the same as the listAllCourses() function.
async function findCoursesWithMinCapacity(cap) {
    let raw = await fs.readFile('courses.json', 'utf8')
    let data = await JSON.parse(raw)
    if (data.length === 0) {
        console.log('No courses found')
    }
    else {
        let output = 'code, name, capacity\n'
        let someOutput = false
        for (c of data) {
            if (c.capacity >= cap) {
                output += `${c.code}, ${c.name}, ${c.capacity}`
                someOutput = true
            }
        }
        if (someOutput) {
            console.log(output)
        }
        else {
            console.log('No courses')
        }
    }

}

// This function will update the capacity of a single course.  If the course code does not exist, print a message
// indicating that no course was found.
async function updateCapacity(code, capacity) {
    let raw = await fs.readFile('courses.json', 'utf8')
    let data = await JSON.parse(raw)
    for (c of data) {
        if (c.code === code) {
            c.capacity = capacity
        }
    }
    let newData = JSON.stringify(data)
    await fs.writeFile('courses.json', newData)
}

async function showMenu() {
    while (true) {
        console.log('Options:')
        console.log('1. List all courses')
        console.log('2. Find course by code')
        console.log('3. Find courses with min capacity')
        console.log('4. Update capacity')
        console.log('5. Quit')
        let selection = Number(prompt("Enter option: "))
        if (selection == 1) {
            await listAllCourses()
        }
        else if (selection == 2){
            let course = prompt("Course code? ")
            await findCourseByCode(course)
        }
        else if (selection == 3) {
            // find a course with a minimum capacity
            let capacity = Number(prompt("What capacity? "))
            await findCoursesWithMinCapacity(capacity)
        }
        else if (selection == 4) {
            // update capacity of a course
            let course = prompt("Course code? ")
            let capacity = Number(prompt("What is the new capacity? "))
            await updateCapacity(course, capacity)
        }
        else if (selection == 5) {
            break // leave the loop
        }
        else {
            console.log('******** ERROR!!! Pick a number between 1 and 5')
        }
    }

}


showMenu()
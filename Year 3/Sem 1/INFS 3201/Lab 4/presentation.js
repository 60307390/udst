const fs = require("fs/promises")
const prompt = require("prompt-sync")()

const business = require("./business")

// This function will display all of the courses currently in the system.
// The output will be:
// CODE, Name, Capacity
// INFS3201, Web Tech II, 34
// INFS1201, Programming, 120
//
// If there are no courses then you should see the message "No courses".
async function listAllCourses() {
    let data = await business.allCourses()
    if (data.length === 0) {
        console.log("No courses found")
        return
    }
    console.log("code, name, capacity")
    for (c of data) {
        console.log(`${c.code}, ${c.name}, ${c.capacity}`)
    }
}

// This function will display a single course given the code (i.e. INFS3201).  The format of the output
// must be:
//    Code: INFS3201
//    Name: Web Technologies II
//    Capacity: 24
// If there is no course with the given code then print the message "Course not found"
async function findCourseByCode(code) {
    let course = await business.findCourse(code)
    if (course === undefined) {
        console.log("No course found")
        return
    }
    console.log(`Code: ${course.code}`)
    console.log(`Name: ${course.name}`)
    console.log(`Capacity: ${course.capacity}`)
    console.log("")
}

// This function will display all courses with a minimum of "cap" capacity.  For example if you put
// the parameter cap at 30, we would see courses with a capacity 30 or larger.  The output should be
// the same as the listAllCourses() function.
async function findCoursesWithMinCapacity(cap) {
    let data = await business.allCourses()
    if (data.length === 0) {
        console.log("No courses found")
        return
    }
    let minCapCourses = await business.minCapacityCourses(cap)

    if (minCapCourses.length === 0) {
        console.log("No courses")
        return
    }

    console.log("code, name, capacity")
    for (let course of minCapCourses) {
        console.log(`${course.code}, ${course.name}, ${course.capacity}`)
    }
}

// This function will update the capacity of a single course.  If the course code does not exist, print a message
// indicating that no course was found.
async function updateCapacity(code, capacity) {
    let success = await business.updateCapacity(code, capacity)
    if (!success) {
        console.log(
            "Unsuccessful capacity change. Capacity maybe invalid or course may not exist.",
        )
        return
    }
    console.log("Capacity successfully updated")
}

async function showMenu() {
    while (true) {
        console.log("Options:")
        console.log("1. List all courses")
        console.log("2. Find course by code")
        console.log("3. Find courses with min capacity")
        console.log("4. Update capacity")
        console.log("5. Quit")
        let selection = Number(prompt("Enter option: "))
        if (selection == 1) {
            await listAllCourses()
        } else if (selection == 2) {
            let course = prompt("Course code? ")
            await findCourseByCode(course)
        } else if (selection == 3) {
            // find a course with a minimum capacity
            let capacity = Number(prompt("What capacity? "))
            await findCoursesWithMinCapacity(capacity)
        } else if (selection == 4) {
            // update capacity of a course
            let course = prompt("Course code? ")
            let capacity = Number(prompt("What is the new capacity? "))
            await updateCapacity(course, capacity)
        } else if (selection == 5) {
            break // leave the loop
        } else {
            console.log("******** ERROR!!! Pick a number between 1 and 5")
        }
    }
}

showMenu()

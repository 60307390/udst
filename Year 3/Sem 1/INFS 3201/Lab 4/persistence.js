const fs = require("fs/promises")

const FILENAME = "courses.json"

async function readCourseData() {
    const raw = await fs.readFile(FILENAME, "utf8")
    const data = await JSON.parse(raw)
    return data
}

async function writeCourseData(data) {
    const newData = JSON.stringify(data)
    await fs.writeFile(FILENAME, newData)
}

async function allCourses() {
    const data = await readCourseData()
    return data
}

async function findCourse(code) {
    const data = await readCourseData()
    let course = undefined
    for (let c of data) {
        if (c.code === code) {
            course = c
        }
    }
    return course
}

async function minCapacityCourses(min) {
    const data = await readCourseData()
    let courses = []
    for (let course of data) {
        if (course.capacity >= min) {
            courses.push(course)
        }
    }
    return courses
}

async function updateCapacity(code, newCap) {
    // const course = findCourse(code);
    // if (course === undefined)
    //     return false;
    const data = await readCourseData()
    let found = false

    for (let c of data) {
        if (c.code === code) {
            found = true
            c.capacity = newCap
        }
    }

    if (!found) return false

    await writeCourseData(data)

    return true
}

module.exports = {
    writeCourseData,
    allCourses,
    findCourse,
    minCapacityCourses,
    updateCapacity,
}

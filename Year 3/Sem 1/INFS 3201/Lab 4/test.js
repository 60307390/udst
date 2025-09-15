const fs = require("fs/promises")
const persistence = require("./persistence")

// const DEBUG_LEVEL = 0
const DEBUG = true

function debugLog(message) {
    if (DEBUG) {
        // console.log("DEBUG: ", message)
        console.log(message)
    }
}

async function testReadWrite() {
    let data = await persistence.allCourses()
    debugLog(data)

    const originalName = data[0].name
    data[0].name = "Cool Systems Management"
    await persistence.writeCourseData(data)
    debugLog(data)

    data[0].name = originalName
    await persistence.writeCourseData(data)
    debugLog(data)
}

async function testFindCourse() {
    let course1 = "INFS2201"
    let course2 = "INFS2200"

    let course1Data = await persistence.findCourse(course1)
    debugLog(course1Data)

    let course2Data = await persistence.findCourse(course2)
    debugLog(course2Data)
}

async function testMinCapacity() {
    let test1Data = await persistence.minCapacityCourses(2)
    debugLog("For capacity = 2")
    debugLog(test1Data)

    let test2Data = await persistence.minCapacityCourses(10)
    debugLog("For capacity = 10")
    debugLog(test2Data)
}

async function testUpdateCapacity() {
    let course1 = "INFS2201"
    let course2 = "INFS2200"

    let data = await persistence.allCourses()
    let course1Details = await persistence.findCourse(course1)
    let course1OriginalCap = course1Details.capacity
    debugLog("Before")
    debugLog(data)

    let course1Success = await persistence.updateCapacity(course1, 12)

    debugLog("After")
    data = await persistence.allCourses()
    debugLog(data)

    await persistence.updateCapacity(course1, course1OriginalCap)

    debugLog("Before")
    data = await persistence.allCourses()
    debugLog(data)

    await persistence.updateCapacity(course2, 10)

    debugLog("After")
    data = await persistence.allCourses()
    debugLog(data)
}

async function main() {
    debugLog("Read/Write test")
    await testReadWrite()

    debugLog("Finding course test")
    await testFindCourse()

    debugLog("Min. capacity courses test")
    await testMinCapacity()

    debugLog("Update capacity test")
    await testUpdateCapacity()
}

main()

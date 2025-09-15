const persistence = require("./persistence")

async function updateCapacity(code, newCap) {
    if (newCap > 100) {
        return false
    }
    return persistence.updateCapacity(code, newCap)
}

async function allCourses() {
    return persistence.allCourses()
}

async function findCourse(code) {
    return persistence.findCourse(code)
}

async function minCapacityCourses(min) {
    return persistence.minCapacityCourses(min)
}

module.exports = {
    allCourses,
    findCourse,
    minCapacityCourses,
    updateCapacity,
}

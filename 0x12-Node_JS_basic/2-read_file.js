const fs = require('fs');

function countStudents(path) {
  if (!fs.existsSync(path)) throw Error('Cannot load the database'); 
  try {
    const inFields = {}; 
    const data = fs.readFileSync(path, 'utf-8').split('\n');

    for (let i = 1; i < data.length; i += 1) {
      const line = data[i].split(',');
      if (inFields[line[3]]) { 
        inFields[line[3]].counter += 1;
        inFields[line[3]].students.push(` ${line[0]}`);
      } else {
        inFields[line[3]] = { counter: 1, students: [`${line[0]}`] };
      }
    }
    console.log(`Number of students: ${data.length - 1}`);
    for (const key in inFields) {
      if (Object.prototype.hasOwnProperty.call(inFields, key)) {
        console.log(`Number of students in ${key}: ${inFields[key].counter}. List: ${inFields[key].students}`);
      }
    }
  } catch (e) {
    throw Error(e);
  }
}
module.exports = countStudents;
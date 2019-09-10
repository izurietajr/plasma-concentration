get_square = () => {
    var {PythonShell} = require('python-shell')
    var path = require('path')

    var number = document.querySelector('#number').value

    var options = {
        scriptPath: path.join(__dirname, 'python/'),
        args: [number]
    }

    PythonShell.run('script.py', options, (err, results) => {
        if (err) throw err
        console.log(results, 'results')
        result = document.querySelector('#result').innerHTML = results[0]
    })
}

document.querySelector('#btn').addEventListener('click', e => {
    get_square()
})

document.querySelector('.delete').addEventListener('click', e => {
    var number = document.querySelector('#number')
    number.value = ''
    result = document.querySelector('#result').innerHTML = ''
})
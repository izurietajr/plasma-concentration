calculate = () => {
    var {PythonShell} = require('python-shell')
    var path = require('path')

    var kab = document.querySelector('#kab').value
    var kel = document.querySelector('#kel').value
    var cdrag = document.querySelector('#cdrag').value
    var kaberr = document.querySelector('#kaberr').value
    var kelerr = document.querySelector('#kelerr').value
    var cdragerr = document.querySelector('#cdragerr').value
    var eerr = document.querySelector('#eerr').value

    var options = {
        scriptPath: path.join(__dirname, 'python/'),
        args: [kab, kel, cdrag, kaberr, kelerr, cdragerr, eerr]
    }

    PythonShell.run('plasma.py', options, (err, results) => {
        if (err) throw err
        console.log(results, 'results')
        result = document.querySelector('#result').innerHTML = results[0]
    })
}

document.querySelector('#btn').addEventListener('click', e => {
    calculate()
})

document.querySelector('.delete').addEventListener('click', e => {

	document.querySelector('#kab').value = ''
	document.querySelector('#kel').value = ''
	document.querySelector('#cdrag').value = ''
	document.querySelector('#kaberr').value = ''
	document.querySelector('#kelerr').value = ''
	document.querySelector('#cdragerr').value = ''
	document.querySelector('#eerr').value = '0.00001'
	document.querySelector('#result').innerHTML = ''
})

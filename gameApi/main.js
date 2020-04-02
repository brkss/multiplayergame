const express = require("express")
const bodyPar = require('body-parser')

const app = express()
players = [];

app.use(bodyPar.urlencoded({ extended: true }))

app.use(bodyPar.json())


app.get('/g/:name', (req, res) => {
    name = req.params.name;
    if (!players.find(x => x.name != name)) {
        console.log(players.find(x => x.name == name))
        res.send([players.find(x => x.name == name)])
    } else {
        console.log(players.find(x => x.name != name))
        res.send([players.find(x => x.name != name)])
    }

})

app.get("/q/:name", (req, res) => {
    let index = players.findIndex(x => x.name == req.body.name)
    players.splice(index, 1)
    console.log("quited")
    console.log(players)
})
app.post('/b', (req, res) => {
    console.log("post");
    if (!req.body.name) {
        return res.status(400).send({
            message: "Player Index can not be found!"
        });
    }
    // Update Player
    if (players.find(x => x.name == req.body.name)) {
        let index = players.findIndex(x => x.name == req.body.name)
        players[index].index = req.body.index
        players[index].x = req.body.x
        players[index].y = req.body.y
        if (req.body.shoot == 'True') {
            players[index].shoot = true
            players[index].bx = req.body.bx
            players[index].by = req.body.by
        } else {
            players[index].shoot = false
            players[index].bx = -1
            players[index].by = -1
        }
        console.log('alerdy exist.')
    } else if (players.length < 2) {
        const player = {
            index: req.body.index || 1 * 8 + 5,
            x: req.body.x,
            y: req.body.y,
            shoot: req.body.shoot,
            bx: req.body.bx,
            by: req.body.by,
            name: req.body.name
        };
        players.push(player)
    } else {
        console.log('room full!')
    }
    return res.status(200).send(players)
});

app.listen(3000, _ => {
    console.log("Server listen at http://localhost:3000 Thank You!")
})
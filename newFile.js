import { app, prisma } from './server';

app.put('/usuarios/:id', async (req, res) => {

    await prisma.user.update({
        data: {
            email: req.body.email,
            name: req.body.name,
            age: req.body.age
        }
    });

    res.status(201).json(req.body);

});

import express from "express";
import cors from "cors";
import { PrismaClient } from "@prisma/client";

export const prisma = new PrismaClient();

export const app = express(); /*const é uma variável*/
app.use(express.json());
app.use(
  cors()
); /*Em uma API profissional precisariamos colocar o endereço do front end*/

app.post("/usuarios", async (req, res) => {
  await prisma.user.create({
    data: {
      email: req.body.email,
      name: req.body.name,
      age: req.body.age,
      dataNascimento: req.body.dataNascimento,
    },
  });

  res.status(201).json(req.body);
});

app.get("/usuarios", async (req, res) => {
  const users = await prisma.user.findMany();

  /*  if (req.query) {
    users = await prisma.user.findMany ({
      where: {
        name: req.query.name,
      }
    })
  }else{
    users = await prisma.user.findMany();  Eu posso usar dessa forma, caso eu queira fazer um filtro*/

  res.status(200).json(users);
});

app.put("/usuarios/:id", async (req, res) => {
  await prisma.user.update({
    where: {
      id: req.params.id,
    },
    data: {
      email: req.body.email,
      name: req.body.name,
      age: req.body.age,
      dataNascimento: req.body.dataNascimento,
    },
  });

  res.status(201).json(req.body);
});

app.delete("/usuarios/:id", async (req, res) => {
  await prisma.user.delete({
    where: {
      id: req.params.id,
    },
  });
  res.status(200).json({ message: "Ususário deletado com sucesso!" });
});

app.listen(3000);

/*Criar nossa API de usuário

 - Criar um ususário
 - Listar todos os usuários
 - Editar um usuário
 - Deletar um usuário
 */

/* usuário mongodb - renatoti
senha - cH52h5VKy3nuCYNr
*/

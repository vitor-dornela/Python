package br.com.vitordornela.todolist.user;

import java.time.LocalDateTime;
import java.util.UUID;

import org.hibernate.annotations.CreationTimestamp;

import jakarta.persistence.Column;
import jakarta.persistence.Entity; // dependencia da JPA para banco de dados
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import lombok.Data; //lombok ajuda a deixar o código limpo sem precisar ficar criando os getters e setters 

@Data
@Entity(name = "tb_users") //cria a tabela. As variaveis abaixo são interpretadas como colunas
public class UserModel {
    @Id //seta como chave primária o id
    @GeneratedValue(generator = "UUID") //formato as5d5sad54as--a5as5-a5a5as-a6sd5a-a5sd6asd6a5a
    private UUID id;
    //@Column(name = "usuario") // se quiser fazer individualmente as colunas
    @Column(unique = true)
    private String username;
    private String name;
    private String password;

    @CreationTimestamp //gera automatico a hora criada
    private LocalDateTime createdAt;


}

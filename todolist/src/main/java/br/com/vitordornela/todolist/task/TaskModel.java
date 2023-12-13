package br.com.vitordornela.todolist.task;

import java.time.LocalDateTime;
import java.util.UUID;

import org.hibernate.annotations.CreationTimestamp;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import lombok.Data;

    /**
     * Descrição das tasks
     * ID
     * Usuário (ID_USUARIO)
     * Descrição
     * Título
     * Data de início
     * Data de término
     * Prioridade
     */
@Data //depend. do Lombok para Setters e Getters
@Entity(name = "tb_tasks") // depend. do Jakarta para criar a tabela "tb_tasks"
public class TaskModel {

    @Id // associa id a chave primária
    @GeneratedValue(generator = "UUID") // gera automaticamente o ID
    private UUID id;
    private String description;

    @Column(length = 50)
    private String title;
    private LocalDateTime startAt;
    private LocalDateTime endAt;
    private String priority;

    @CreationTimestamp // gera automaticamente uma marcação de tempo quando uma nova entidade é criada e persistida na database
    private LocalDateTime createdAt;

    private UUID idUser;

}

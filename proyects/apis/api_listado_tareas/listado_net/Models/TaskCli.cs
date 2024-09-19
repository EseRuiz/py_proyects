using System;
using System.ComponentModel.DataAnnotations;

namespace listado_net.Models  
{
    public enum TaskState
    {
        TODO,
        IN_PROGRESS,
        DONE
    }
    public class TaskCli  
    {
        public Guid Id { get; set; }

        [Required(ErrorMessage = "El nombre de la tarea es obligatorio")]
        [StringLength(150, ErrorMessage = "El nombre no puede exceder los 150 caracteres")]
        public string TaskName { get; set; }  

        [Required(ErrorMessage = "El estado del progreso es obligatorio")]
        [StringLength(15, ErrorMessage = "El nombre no puede exceder los 15 caracteres")]
        public TaskState Status { get; set; } 

        public DateTime CreatedAt { get; set; }  
        public DateTime UpdatedAt { get; set; }  

        public TaskCli()  
        {
            Id = Guid.NewGuid();
            CreatedAt = DateTime.UtcNow;  
            UpdatedAt = DateTime.UtcNow;  
        }
    }
}

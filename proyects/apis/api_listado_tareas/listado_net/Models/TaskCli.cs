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

        [Required]
        public string TaskName { get; set; }  

        [Required]
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

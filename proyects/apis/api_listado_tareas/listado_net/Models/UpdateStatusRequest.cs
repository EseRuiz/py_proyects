using System.ComponentModel.DataAnnotations;
using listado_net.Models; 

public class UpdateStatusRequest
{
    [Required]
    public TaskState Status { get; set; }
}

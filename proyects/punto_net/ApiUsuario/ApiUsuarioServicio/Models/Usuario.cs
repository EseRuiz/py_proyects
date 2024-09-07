using System.ComponentModel.DataAnnotations;

namespace MiApiDeServicios.Models
{
    public class Usuario
    {   
        public int Id { get; set; }
        
        [Required(ErrorMessage = "El nombre es obligatorio")]
        [StringLength(150, ErrorMessage = "El nombre no puede exceder los 100 caracteres")]
        public required string Nombre { get; set; }

        [Phone(ErrorMessage = "El número de teléfono no es válido")]
        [Required(ErrorMessage = "El teléfono es obligatorio")]
        public required string Telefono { get; set; }

        [Required(ErrorMessage = "El país es obligatorio")]
        public required string Pais { get; set; }

        [Required(ErrorMessage = "El departamento es obligatorio")]
        public required string Departamento { get; set; }

        [Required(ErrorMessage = "El municipio es obligatorio")]
        public required string Municipio { get; set; }

        [Required(ErrorMessage = "La dirección es obligatoria")]
        [StringLength(124, ErrorMessage = "La dirección no puede exceder los 125 caracteres")]
        public required string Direccion { get; set; }
    }
}

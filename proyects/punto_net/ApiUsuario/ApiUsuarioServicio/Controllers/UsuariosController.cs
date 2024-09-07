using Microsoft.AspNetCore.Mvc;
using MiApiDeServicios.Models;

namespace MiApiDeServicios.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class UsuariosController : ControllerBase
    {
        private static List<Usuario> usuarios = new List<Usuario>();

        
        [HttpPost("registrar")]
        public IActionResult RegistrarUsuario([FromBody] Usuario usuario)
        {
            usuarios.Add(usuario);
            return Ok(new { mensaje = "Usuario registrado exitosamente", usuario });
        }

        [HttpGet("verificar")]
        public IActionResult ObtenerUsuarios()
        {
            return Ok(usuarios);
        }

        [HttpGet("{id}")]
        public IActionResult ObtenerUsuarioPorId(int id)
        {
            var usuario = usuarios.FirstOrDefault(u => u.Id == id);
            if (usuario == null)
            {
                return NotFound(new { mensaje = "Usuario no encontrado" });
            }
            return Ok(usuario);
        }

        [HttpPatch("{id}")]
        public IActionResult ActualizarUsuarioParcial(int id, [FromBody] Usuario usuarioActualizado)
        {
            var usuarioExistente = usuarios.FirstOrDefault(u => u.Id == id);
            if (usuarioExistente == null)
            {
                return NotFound(new { mensaje = "Usuario no encontrado" });
            }

            if (!string.IsNullOrEmpty(usuarioActualizado.Nombre))
                usuarioExistente.Nombre = usuarioActualizado.Nombre;
            if (!string.IsNullOrEmpty(usuarioActualizado.Telefono))
                usuarioExistente.Telefono = usuarioActualizado.Telefono;
            if (!string.IsNullOrEmpty(usuarioActualizado.Pais))
                usuarioExistente.Pais = usuarioActualizado.Pais;
            if (!string.IsNullOrEmpty(usuarioActualizado.Departamento))
                usuarioExistente.Departamento = usuarioActualizado.Departamento;
            if (!string.IsNullOrEmpty(usuarioActualizado.Municipio))
                usuarioExistente.Municipio = usuarioActualizado.Municipio;
            if (!string.IsNullOrEmpty(usuarioActualizado.Direccion))
                usuarioExistente.Direccion = usuarioActualizado.Direccion;

            return Ok(new { mensaje = "Usuario actualizado exitosamente", usuarioExistente });
        }


        [HttpDelete("{id}")]
        public IActionResult EliminarUsuario(int id)
        {
            var usuarioExistente = usuarios.FirstOrDefault(u => u.Id == id);
            if (usuarioExistente == null)
            {
                return NotFound(new { mensaje = "Usuario no encontrado" });
            }

            usuarios.Remove(usuarioExistente);
            return Ok(new { mensaje = "Usuario eliminado exitosamente" });
        }
    }
}

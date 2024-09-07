using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore; // Asegúrate de que esto esté presente
using MiApiDeServicios.Data;
using MiApiDeServicios.Models;
using System.Threading.Tasks;

namespace MiApiDeServicios.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class UsuariosController : ControllerBase
    {
        private readonly ApplicationDbContext _context;

        public UsuariosController(ApplicationDbContext context)
        {
            _context = context;
        }

        [HttpPost("registrar")]
        public async Task<IActionResult> RegistrarUsuario([FromBody] Usuario usuario)
        {
            if (!ModelState.IsValid)
                return BadRequest(ModelState);

            _context.Usuarios.Add(usuario);
            await _context.SaveChangesAsync();
            return Ok(new { mensaje = "Usuario registrado exitosamente", usuario });
        }

        [HttpGet("verificar")]
        public async Task<IActionResult> GetTodosUsuarios()
        {
            var usuarios = await _context.Usuarios.ToListAsync();
            return Ok(usuarios);
        }

        [HttpGet("{id}")]
        public async Task<IActionResult> GetUsuario(int id)
        {
            var usuario = await _context.Usuarios.FindAsync(id);
            if (usuario == null)
                return NotFound();

            return Ok(usuario);
        }

        [HttpPatch("{id}")]
        public async Task<IActionResult> UpdateUsuario(int id, [FromBody] Usuario usuarioActualizado)
        {
            var usuario = await _context.Usuarios.FindAsync(id);
            if (usuario == null)
                return NotFound();

            if (!string.IsNullOrEmpty(usuarioActualizado.Nombre))
                usuario.Nombre = usuarioActualizado.Nombre;

            if (!string.IsNullOrEmpty(usuarioActualizado.Telefono))
                usuario.Telefono = usuarioActualizado.Telefono;

            if (!string.IsNullOrEmpty(usuarioActualizado.Direccion))
                usuario.Direccion = usuarioActualizado.Direccion;

            await _context.SaveChangesAsync();
            return Ok(new { mensaje = "Usuario actualizado exitosamente", usuario });
        }

        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteUsuario(int id)
        {
            var usuario = await _context.Usuarios.FindAsync(id);
            if (usuario == null)
                return NotFound();

            _context.Usuarios.Remove(usuario);
            await _context.SaveChangesAsync();
            return Ok(new { mensaje = "Usuario eliminado exitosamente" });
        }
    }
}

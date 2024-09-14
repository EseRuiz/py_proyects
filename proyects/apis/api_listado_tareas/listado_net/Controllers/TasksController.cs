using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using listado_net.Data;
using listado_net.Models;
using System;
using System.Linq;
using System.Threading.Tasks;

namespace listado_net.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class TaskCliController : ControllerBase
    {
        private readonly ApplicationDbContext _context;

        public TaskCliController(ApplicationDbContext context)
        {
            _context = context;
        }
        //http://localhost:5050/api/taskcli/registrar
        [HttpPost("registrar")]
        public async Task<IActionResult> RegistrarTarea([FromBody] TaskCli task)
        {
            if (!ModelState.IsValid)
                return BadRequest(ModelState);
            if (!Enum.IsDefined(typeof(TaskState), task.Status))
                return BadRequest("Estado de tarea inválido.");
            _context.Tasks.Add(task);
            await _context.SaveChangesAsync();
            return Ok(new { mensaje = "Tarea registrada exitosamente", task });
        }
        //http://localhost:5050/api/taskcli/verificar
        [HttpGet("verificar")]
        public async Task<IActionResult> GetTodasTareas()
        {
            var tasks = await _context.Tasks.ToListAsync();
            return Ok(tasks);
        }
        //http://localhost:5050/api/taskcli/{id}
        [HttpGet("{id}")]
        public async Task<IActionResult> GetTarea(Guid id)  // busqueda por uuid
        {
            var task = await _context.Tasks.FindAsync(id);
            if (task == null)
                return NotFound();

            return Ok(task);
        }
        //http://localhost:5050/api/taskcli/{id}
        [HttpPut("{id}")]
        public async Task<IActionResult> UpdateTarea(Guid id, [FromBody] TaskCli updatedTask)
        {
            var task = await _context.Tasks.FindAsync(id);
            if (task == null)
                return NotFound();

            task.TaskName = updatedTask.TaskName;
            task.Status = updatedTask.Status;
            task.UpdatedAt = DateTime.UtcNow;

            await _context.SaveChangesAsync();
            return Ok(new { mensaje = "Tarea actualizada exitosamente", task });
        }
        //http://localhost:5050/api/taskcli/status/{status}
        [HttpGet("status/{status}")]
        public async Task<IActionResult> GetTareasPorEstado([FromRoute] TaskState status)  
        {
            var tasks = await _context.Tasks.Where(t => t.Status == status).ToListAsync();
            return Ok(tasks);
        }
        //http://localhost:5050/api/taskcli/{id}/status
        [HttpPatch("{id}/status")]
        public async Task<IActionResult> UpdateStatus(Guid id, [FromBody] UpdateStatusRequest request)
        {
            var task = await _context.Tasks.FindAsync(id);
            if (task == null)
                return NotFound();

            task.Status = request.Status;
            task.UpdatedAt = DateTime.UtcNow;

            await _context.SaveChangesAsync();
            return Ok(new { mensaje = "Estado actualizado exitosamente", task });
        }
        //http://localhost:5050/api/taskcli/{id}
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteTarea(Guid id)
        {
            var task = await _context.Tasks.FindAsync(id);
            if (task == null)
                return NotFound();

            _context.Tasks.Remove(task);
            await _context.SaveChangesAsync();
            return Ok(new { mensaje = "Tarea eliminada exitosamente" });
        }
    }
}

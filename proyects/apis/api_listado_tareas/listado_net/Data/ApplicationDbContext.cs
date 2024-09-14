using Microsoft.EntityFrameworkCore;
using listado_net.Models;  

namespace listado_net.Data  
{
    public class ApplicationDbContext : DbContext
    {
        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
            : base(options)
        {
        }

        public DbSet<TaskCli> Tasks { get; set; }  
    }
}
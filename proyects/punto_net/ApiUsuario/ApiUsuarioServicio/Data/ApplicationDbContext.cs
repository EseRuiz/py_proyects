using Microsoft.EntityFrameworkCore;
using MiApiDeServicios.Models;

namespace MiApiDeServicios.Data
{
    public class ApplicationDbContext : DbContext
    {
        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
            : base(options)
        {
        }

        public DbSet<Usuario> Usuarios { get; set; }
    }
}
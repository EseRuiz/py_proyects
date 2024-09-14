using System;
using System.Text.Json;
using System.Text.Json.Serialization;
using listado_net.Models;

public class TaskStateConverter : JsonConverter<TaskState>
{
    public override TaskState Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
    {
        var value = reader.GetString();
        return Enum.TryParse(value, true, out TaskState result) ? result : throw new JsonException($"Invalid value for TaskState: {value}");
    }

    public override void Write(Utf8JsonWriter writer, TaskState value, JsonSerializerOptions options)
    {
        writer.WriteStringValue(value.ToString());
    }
}

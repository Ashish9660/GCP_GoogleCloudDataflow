import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions
from args import parser


path_args, pipeline_args = parser.parse_known_args()

input_pattern = path_args.input
output_prefix = path_args.output

options = PipelineOptions(pipeline_args)
p = beam.Pipeline(options=options)

get_count = (
    p
    | 'read input text' >> beam.io.ReadFromText(input_pattern)
    | 'Apply Fiter' >> beam.Filter(lambda x: 'name' not in x)
    | 'write to text' >> beam.io.WriteToText(output_prefix,file_name_suffix='ParDo_test.csv',shard_name_template='')
)

p.run()
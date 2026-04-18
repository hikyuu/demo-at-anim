meta:
  id: bild
  title: Klei Build
  endian: le
  encoding: UTF-8
  # See: https://github.com/kleientertainment/ds_mod_tools/blob/master/pkg/unix/mod_tools/tools/scripts/buildanimation.py
seq:
- id: magic
  contents: "BILD"
- id: version
  type: u4
- id: num_symbols
  type: u4
- id: num_frames
  type: u4
- id: len_build_name
  type: u4
- id: build_name
  size: len_build_name
  type: str
- id: num_materials
  type: u4
- id: materials
  type: material
  repeat: expr
  repeat-expr: num_materials
- id: symbols
  type: symbol
  repeat: expr
  repeat-expr: num_symbols
- id: num_vertices
  type: u4
- id: vertices
  type: vertex
  repeat: expr
  repeat-expr: num_vertices
- id: num_hashed_strings
  type: u4
- id: hashed_strings
  type: hashed_string
  repeat: expr
  repeat-expr: num_hashed_strings
- id: tail
  size-eos: true
types:
  material:
    seq:
    - id: len_material_texture_name
      type: u4
    - id: material_texture_name
      size: len_material_texture_name
      type: str
  symbol:
    seq:
    - id: symbol_hash
      type: u4
    - id: num_frames
      type: u4
    - id: frames
      type: frame
      repeat: expr
      repeat-expr: num_frames
  frame:
    seq:
    - id: frame_num
      type: u4
    - id: duration
      type: u4
    - id: x
      type: f4
    - id: y
      type: f4
    - id: w
      type: f4
    - id: h
      type: f4
    - id: vb_start_index
      type: u4
    - id: num_verts
      type: u4
  vertex:
    seq:
    - id: x
      type: f4
    - id: y
      type: f4
    - id: z
      type: f4
    - id: u
      type: f4
    - id: v
      type: f4
    - id: w
      type: f4
  hashed_string:
    seq:
    - id: hash
      type: u4
    - id: len_original_string
      type: u4
    - id: original_string
      size: len_original_string
      type: str

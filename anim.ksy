meta:
  id: anim
  title: Klei Animation
  endian: le
  encoding: UTF-8
  # See: https://github.com/kleientertainment/ds_mod_tools/blob/master/pkg/unix/mod_tools/tools/scripts/buildanimation.py
seq:
- id: magic
  contents: "ANIM"
- id: version
  type: u4
- id: num_elements
  type: u4
- id: num_frames
  type: u4
- id: num_events
  type: u4
- id: num_anims
  type: u4
- id: anims
  type: anim
  repeat: expr
  repeat-expr: num_anims
- id: num_hashed_strings
  type: u4
- id: hashed_strings
  type: hashed_string
  repeat: expr
  repeat-expr: num_hashed_strings
- id: tail
  size-eos: true
types:
  mat:
    seq:
    - id: a
      type: f4
    - id: b
      type: f4
    - id: c
      type: f4
    - id: d
      type: f4
    - id: tx
      type: f4
    - id: ty
      type: f4
    - id: z
      type: f4
    - id: unknown_value
      type: f4
      if: _root.version == 6
    - id: sa
      type: f4
    - id: sb
      type: f4
    - id: sc
      type: f4
    - id: sd
      type: f4
    - id: stx
      type: f4
    - id: sty
      type: f4
    - id: sz
      type: f4
  event:
    seq:
    - id: event_hash
      type: u4
  element:
    seq:
    - id: symbol_hash
      type: u4
    - id: symbol_frame
      type: u4
    - id: folder_hash
      type: u4
    - id: unknown_value
      type: f4
      if: _root.version == 5
    - id: unknown_hash
      type: u4
      if: _root.version == 6
    - id: mat
      type: mat
  frame:
    seq:
    - id: x
      type: f4
    - id: y
      type: f4
    - id: w
      type: f4
    - id: h
      type: f4
    - id: num_events
      type: u4
    - id: events
      repeat: expr
      repeat-expr: num_events
      type: event
    - id: num_elements
      type: u4
    - id: elements
      repeat: expr
      repeat-expr: num_elements
      type: element
  anim:
    seq:
    - id: len_name
      type: u4
    - id: name
      size: len_name
      type: str
    - id: validfacings
      type: u1
    - id: root_symbol_hash
      type: u4
    - id: frame_rate
      type: f4
    - id: num_frames
      type: u4
    - id: frames
      repeat: expr
      repeat-expr: num_frames
      type: frame
  hashed_string:
    seq:
    - id: hash
      type: u4
    - id: len_original_string
      type: u4
    - id: original_string
      size: len_original_string
      type: str

package config

import (
	"encoding/json"

	"moul.io/assh/pkg/hooks"
)

// HostHooks represents a static list of Hooks
type HostHooks struct {
	AfterConfigWrite  hooks.Hooks `yaml:"afterconfigwrite,omitempty,flow" json:"AfterConfigWrite,omitempty"`
	BeforeConfigWrite hooks.Hooks `yaml:"beforeconfigwrite,omitempty,flow" json:"BeforeConfigWrite,omitempty"`
	BeforeConnect     hooks.Hooks `yaml:"beforeconnect,omitempty,flow" json:"BeforeConnect,omitempty"`
	OnConnect         hooks.Hooks `yaml:"onconnect,omitempty,flow" json:"OnConnect,omitempty"`
	OnProxyConnect    hooks.Hooks `yaml:"onproxyconnect,omitempty,flow" json:"OnProxyConnect,omitempty"`
	OnConnectError    hooks.Hooks `yaml:"onconnecterror,omitempty,flow" json:"OnConnectError,omitempty"`
	OnDisconnect      hooks.Hooks `yaml:"ondisconnect,omitempty,flow" json:"OnDisconnect,omitempty"`
}

// Length returns the quantity of hooks of any type
func (hh *HostHooks) Length() int {
	if hh == nil {
		return 0
	}
	return len(hh.AfterConfigWrite) +
		len(hh.BeforeConnect) +
		len(hh.OnConnectError) +
		len(hh.OnDisconnect) +
		len(hh.OnConnect) +
		len(hh.OnProxyConnect)
}

// String returns the JSON output
func (hh *HostHooks) String() string {
	s, err := json.Marshal(hh)
	if err != nil {
		return err.Error()
	}
	return string(s)
}
